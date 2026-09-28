#!/usr/bin/env python3
"""
Local defensive scanner for agent skill packages.

This is a stdlib-only implementation inspired by Sentry's public skill-scanner
workflow. It is intentionally read-only and redacts secret evidence by default.
"""

from __future__ import annotations

import argparse
import base64
import fnmatch
import json
import re
import struct
from pathlib import Path
from urllib.parse import urlparse

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".sh", ".bash", ".zsh", ".js", ".ts", ".json",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".xml", ".html",
    ".htm", ".ps1", ".bat", ".cmd",
}
SCRIPT_SUFFIXES = {".py", ".sh", ".bash", ".zsh", ".js", ".ts", ".ps1", ".bat", ".cmd"}

PROMPT_PATTERNS = [
    (re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.I), "instruction override", "critical"),
    (re.compile(r"disregard\s+(all\s+)?(previous|prior|above)\s+(instructions|rules|guidelines)", re.I), "instruction override", "critical"),
    (re.compile(r"forget\s+(all\s+)?(previous|prior|your)\s+(instructions|rules|training)", re.I), "instruction override", "critical"),
    (re.compile(r"enter\s+(developer|debug|admin|god)\s+mode", re.I), "jailbreak mode request", "critical"),
    (re.compile(r"bypass\s+(safety|security|content|filter|restriction)", re.I), "safety bypass request", "critical"),
    (re.compile(r"new\s+system\s+(prompt|instruction|message)\s*:", re.I), "new system prompt", "critical"),
    (re.compile(r"from\s+now\s+on,?\s+(you|ignore|forget|disregard)", re.I), "persistent instruction override", "high"),
    (re.compile(r"output\s+(your|the)\s+(system|initial|original)\s+(prompt|instructions)", re.I), "system prompt extraction", "high"),
]

SECRET_PATTERNS = [
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key id", "critical"),
    (re.compile(r"\bgh[pso]_[0-9A-Za-z]{30,}\b"), "GitHub token", "critical"),
    (re.compile(r"\bgithub_pat_[0-9A-Za-z_]{40,}\b"), "GitHub fine-grained token", "critical"),
    (re.compile(r"\bsk-ant-[0-9A-Za-z_-]{40,}\b"), "Anthropic API key", "critical"),
    (re.compile(r"\bxox[bpors]-[0-9A-Za-z-]{10,}\b"), "Slack token", "critical"),
    (re.compile(r"-----BEGIN\s+(RSA\s+|EC\s+|OPENSSH\s+)?PRIVATE\s+KEY-----", re.I), "private key", "critical"),
    (re.compile(r"(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{8,}['\"]", re.I), "hardcoded password", "high"),
    (re.compile(r"(api[_-]?key|secret|token)\s*[:=]\s*['\"][0-9A-Za-z_./+=:-]{16,}['\"]", re.I), "hardcoded secret/token", "high"),
]

DANGEROUS_CODE_PATTERNS = [
    (re.compile(r"\beval\s*\("), "eval() execution", "high"),
    (re.compile(r"\bexec\s*\("), "exec() execution", "high"),
    (re.compile(r"subprocess.*shell\s*=\s*True", re.I), "subprocess shell=True", "high"),
    (re.compile(r"\bos\.(system|popen)\s*\(", re.I), "OS command execution", "high"),
    (re.compile(r"\b(socket\.(connect|create_connection)|/dev/tcp/)\b", re.I), "raw network connection", "high"),
    (re.compile(r"\b(nc|ncat|netcat)\b.*(-e|/bin/(ba)?sh)", re.I), "possible reverse shell", "critical"),
    (re.compile(r"\b(curl|wget)\b", re.I), "network download/upload command", "medium"),
    (re.compile(r"\brequests\.(get|post|put|patch|delete)\s*\(", re.I), "HTTP request", "medium"),
    (re.compile(r"(HOME|USERPROFILE|Path\.home\(\)).*(\.ssh|credentials|\.netrc|\.pgpass)", re.I), "sensitive path access", "high"),
    (re.compile(r"(write_text|open\s*\().*(settings\.json|MEMORY\.md|\.mcp\.json|\.git/hooks|\.bashrc|\.zshrc)", re.I), "persistent config or hook modification", "critical"),
]

TRUSTED_DOMAINS = {
    "github.com", "api.github.com", "raw.githubusercontent.com",
    "pypi.org", "npmjs.com", "crates.io",
    "docs.python.org", "developer.mozilla.org",
    "sentry.io", "docs.sentry.io", "develop.sentry.dev",
    "agentskills.io",
}

TEST_PATTERNS = ("conftest.py", "test_*.py", "*_test.py", "*.test.js", "*.test.ts")


def sanitize_evidence(value: str) -> str:
    clean = str(value).strip()
    for pattern, _desc, _severity in SECRET_PATTERNS:
        clean = pattern.sub("[REDACTED]", clean)
    clean = re.sub(
        r"(?i)(https?://)([^/\s:@]+):([^@\s/]+)@",
        r"\1[REDACTED]@",
        clean,
    )
    clean = re.sub(
        r"(?i)([?&](?:access[_-]?token|api[_-]?key|apikey|key|secret|token|password|passwd|pwd)=)[^&#\s]+",
        r"\1[REDACTED]",
        clean,
    )
    return clean[:200]


def safe_report_url(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    netloc = host
    try:
        if parsed.port is not None:
            netloc = f"{netloc}:{parsed.port}"
    except ValueError:
        pass
    safe = f"{parsed.scheme}://{netloc}{parsed.path}"
    if parsed.query:
        safe += "?[REDACTED]"
    return sanitize_evidence(safe)


def add(findings, *, kind, severity, category, location, issue, evidence=None):
    item = {
        "type": kind,
        "severity": severity,
        "category": category,
        "location": location,
        "issue": sanitize_evidence(issue),
    }
    if evidence is not None:
        item["evidence"] = sanitize_evidence(evidence)
    findings.append(item)


def redact_line(line: str, pattern: re.Pattern[str]) -> str:
    return sanitize_evidence(pattern.sub("[REDACTED]", line.strip()))


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data = {}
    current = None
    for raw in parts[1].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace() and current:
            data[current] = f"{data[current]} {raw.strip()}".strip()
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        current = key.strip()
        data[current] = value.strip().strip("\"'")
    return data


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.name == "SKILL.md" or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def scan_text(path: Path, rel: str, findings: list[dict], urls: list[dict]):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        add(findings, kind="Read Error", severity="medium", category="Validation",
            location=rel, issue=str(exc))
        return

    for lineno, line in enumerate(text.splitlines(), 1):
        loc = f"{rel}:{lineno}"
        for pattern, desc, severity in SECRET_PATTERNS:
            if pattern.search(line):
                add(findings, kind="Secret Detected", severity=severity,
                    category="Secret Exposure", location=loc, issue=desc,
                    evidence=redact_line(line, pattern))
                break

        for pattern, desc, severity in PROMPT_PATTERNS:
            if pattern.search(line):
                add(findings, kind="Prompt Injection Pattern", severity=severity,
                    category="Prompt Injection", location=loc, issue=desc,
                    evidence=line)
                break

        if path.suffix.lower() in SCRIPT_SUFFIXES:
            for pattern, desc, severity in DANGEROUS_CODE_PATTERNS:
                if pattern.search(line):
                    add(findings, kind="Dangerous Code Pattern", severity=severity,
                        category="Script Safety", location=loc, issue=desc,
                        evidence=line)
                    break

        for url in re.findall(r"https?://[^\s\)\]\>\"'`]+", line):
            clean = url.rstrip(".,;:")
            host = (urlparse(clean).hostname or "").lower()
            trusted = host in TRUSTED_DOMAINS or any(host.endswith("." + d) for d in TRUSTED_DOMAINS)
            urls.append({
                "url": safe_report_url(clean),
                "host": host,
                "trusted": trusted,
                "location": loc,
            })

    if re.search(r"[\u200b\u200c\u200d\u2060\ufeff]", text):
        add(findings, kind="Zero-Width Characters", severity="high", category="Obfuscation",
            location=rel, issue="Invisible zero-width characters detected")
    if re.search(r"[\u202a-\u202e\u2066-\u2069]", text):
        add(findings, kind="Bidirectional Override", severity="high", category="Obfuscation",
            location=rel, issue="Bidirectional override/isolate characters detected")
    tag_chars = re.findall(r"[\U000e0001-\U000e007f]", text)
    if tag_chars:
        add(findings, kind="Unicode Tag Smuggling", severity="critical", category="Obfuscation",
            location=rel, issue=f"{len(tag_chars)} invisible Unicode tag characters detected")

    for match in re.finditer(r"[A-Za-z0-9+/]{40,}={0,2}", text):
        try:
            decoded = base64.b64decode(match.group(), validate=False).decode("utf-8", errors="ignore")
        except Exception:
            continue
        if any(k in decoded.lower() for k in ("ignore", "system prompt", "eval(", "exec(", "password", "secret", "token")):
            line = text[:match.start()].count("\n") + 1
            add(findings, kind="Suspicious Base64", severity="high", category="Obfuscation",
                location=f"{rel}:{line}", issue="Base64 decodes to security-sensitive instruction/code")


def scan_png(path: Path, rel: str, findings: list[dict]):
    try:
        data = path.read_bytes()
    except OSError:
        return
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return
    offset = 8
    try:
        while offset + 12 <= len(data):
            length = struct.unpack(">I", data[offset:offset + 4])[0]
            ctype = data[offset + 4:offset + 8]
            chunk = data[offset + 8:offset + 8 + length]
            if ctype in (b"tEXt", b"iTXt") and chunk.strip(b"\x00"):
                add(findings, kind="PNG Text Metadata", severity="high", category="Image Injection",
                    location=rel, issue=f"{ctype.decode()} metadata present; inspect before multimodal use")
            offset += 12 + length
    except (struct.error, ValueError):
        return


def scan_skill(root: Path) -> dict:
    root = root.resolve()
    skill_md = root / "SKILL.md"
    findings: list[dict] = []
    urls: list[dict] = []

    if not skill_md.is_file():
        return {"error": f"No SKILL.md found in {root}"}

    skill_text = skill_md.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(skill_text)
    if not fm:
        add(findings, kind="Invalid Frontmatter", severity="high", category="Validation",
            location="SKILL.md:1", issue="Missing or unparseable frontmatter")
    else:
        if not fm.get("name"):
            add(findings, kind="Missing Name", severity="high", category="Validation",
                location="SKILL.md", issue="Required name is missing")
        elif fm["name"] != root.name:
            add(findings, kind="Name Mismatch", severity="medium", category="Validation",
                location="SKILL.md", issue=f"name '{fm['name']}' differs from directory '{root.name}'")
        if not fm.get("description"):
            add(findings, kind="Missing Description", severity="medium", category="Validation",
                location="SKILL.md", issue="Required description is missing")
        tools = fm.get("allowed-tools", "")
        if tools.strip() == "*":
            add(findings, kind="Unrestricted Tools", severity="critical",
                category="Excessive Permissions", location="SKILL.md",
                issue="allowed-tools grants unrestricted tool access")
        if "hooks" in fm:
            add(findings, kind="Frontmatter Hooks", severity="critical",
                category="Hook Execution", location="SKILL.md",
                issue="Lifecycle hooks require explicit review before adoption")

    for lineno, line in enumerate(skill_text.splitlines(), 1):
        if re.search(r"!\`[^`]+\`", line):
            add(findings, kind="Pre-prompt Command", severity="high",
                category="Pre-prompt Execution", location=f"SKILL.md:{lineno}",
                issue="Command-like template syntax can execute before model review",
                evidence=line)

    for path in sorted(root.rglob("*")):
        rel = str(path.relative_to(root))
        if path.is_symlink():
            try:
                target = path.resolve()
                internal = target.is_relative_to(root)
            except (OSError, RuntimeError):
                internal = False
                target = "<unresolved>"
            add(findings, kind="Symlink Detected",
                severity="medium" if internal else "critical",
                category="Symlink Safety", location=rel,
                issue=f"Symlink resolves to {target}; {'inside' if internal else 'outside'} skill root")
            continue
        if path.is_file():
            if any(fnmatch.fnmatch(path.name, p) for p in TEST_PATTERNS):
                add(findings, kind="Auto-discovered Test File", severity="high",
                    category="Implicit Execution", location=rel,
                    issue="Test runners may execute this file automatically")
            if path.name == "package.json":
                try:
                    pkg = json.loads(path.read_text(encoding="utf-8", errors="replace"))
                    scripts = pkg.get("scripts") or {}
                    for hook in ("preinstall", "install", "postinstall", "preuninstall", "postuninstall"):
                        if hook in scripts:
                            add(findings, kind="Package Lifecycle Hook", severity="critical",
                                category="Supply Chain", location=rel,
                                issue=f"package.json defines {hook}: {scripts[hook]}")
                except (OSError, json.JSONDecodeError):
                    pass
            if path.suffix.lower() == ".png":
                scan_png(path, rel, findings)

    for path in iter_text_files(root):
        scan_text(path, str(path.relative_to(root)), findings, urls)

    counts: dict[str, int] = {}
    for item in findings:
        sev = item["severity"]
        counts[sev] = counts.get(sev, 0) + 1

    return {
        "skill_name": fm.get("name", root.name) if fm else root.name,
        "skill_dir": str(root),
        "files_scanned": sum(1 for _ in iter_text_files(root)),
        "findings": findings,
        "finding_counts": counts,
        "total_findings": len(findings),
        "urls": {
            "total": len(urls),
            "untrusted": [u for u in urls if not u["trusted"]],
            "trusted_count": sum(1 for u in urls if u["trusted"]),
        },
        "scanner": {
            "stdlib_only": True,
            "recursive": True,
            "secret_evidence_redacted": True,
            "read_only": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Defensive static scanner for agent skill packages")
    parser.add_argument("skill_directory", help="Directory containing SKILL.md")
    args = parser.parse_args()
    root = Path(args.skill_directory)
    if not root.is_dir():
        print(json.dumps({"error": f"Not a directory: {root}"}))
        return 2
    result = scan_skill(root)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if "error" in result else 0


if __name__ == "__main__":
    raise SystemExit(main())
