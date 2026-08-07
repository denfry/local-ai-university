# Security Policy

## Scope

Local AI University runs a local LLM (via Ollama), executes
LLM-generated code in a sandbox, and fetches content from the web. See
[docs/security.md](docs/security.md) for the full threat model: prompt
injection from untrusted web content, the code sandbox's limitations,
and configurable safety limits.

**The default subprocess code sandbox is not a security boundary against
hostile/adversarial code.** Do not run this project against untrusted
LLM-generated code you don't expect to at least attempt to be
well-intentioned, and do not treat the sandbox as suitable for isolating
genuinely malicious payloads.

## Reporting a vulnerability

If you find a security issue (e.g. a way for fetched web content to
escape the "untrusted data" boundary and cause tool execution, a sandbox
escape, or a way for secrets to leak into logs or Obsidian notes), please
**do not open a public issue**. Instead, use GitHub's private vulnerability
reporting for this repository (Security tab -> "Report a vulnerability").

Please include:

- A description of the issue and its impact.
- Steps to reproduce, or a minimal example.
- The affected version/commit.

We'll acknowledge reports as soon as we can and keep you updated as the
issue is investigated and fixed.

## Supported versions

This project is pre-release (0.x). Security fixes land on the `main`
branch; there is no long-term-support branch at this stage.
