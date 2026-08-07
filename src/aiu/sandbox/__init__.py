"""Code execution sandbox abstraction.

Planned design (see docs/security.md):

- `CodeSandbox` — abstract interface for running LLM-generated code and
  returning results/errors, never via unrestricted `exec()` in the main
  process.
- Default `SubprocessSandbox` — runs code in a temp directory with a
  strict timeout, a restricted/empty environment (no secrets, no `.env`,
  no SSH keys, no host filesystem access beyond the temp dir), clearly
  documented as NOT a security boundary against hostile code.
- Optional `DockerSandbox` — stronger isolation when Docker is available,
  never required for basic installation, and never given access to the
  Docker socket itself.

No sandbox execution logic is implemented yet.
"""
