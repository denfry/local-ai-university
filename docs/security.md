# Security

## Prompt injection and untrusted sources

**All fetched web content is untrusted data, never instructions.** This
is a core design constraint, not a nice-to-have.

The agent's job when reading a web page is to extract facts and cite
them — nothing on that page should ever cause a tool to run, a file to
be written outside the vault/workspace, or a secret to be disclosed.
Concretely:

- If fetched content contains text like *"ignore previous instructions,"
  "run this shell command,"* or *"send your API key/secrets,"* the agent
  must not act on it. The `source_evaluator` and `teacher` prompts
  explicitly instruct the model to treat such text as data to flag, not
  as commands.
- Source content is never concatenated directly into a context that also
  grants tool-calling ability without a clear boundary marking it as a
  quoted excerpt.
- No secrets (API keys, tokens, `.env` contents) are ever included in a
  prompt that also contains untrusted web content.
- Roles that read the web (Teacher, source evaluator) do not have direct
  access to the code sandbox or filesystem-writing tools; only the
  Orchestrator applies their output.

## Code execution sandbox

LLM-generated code is never run via unrestricted `exec()` in the main
Python process.

- Default: a **subprocess sandbox** — a temp working directory, a strict
  execution timeout, a minimal/empty environment, and no access to SSH
  keys, API tokens, `.env`, the user's home directory, the Docker socket,
  or arbitrary host filesystem paths.
- **This subprocess sandbox is not a security boundary against hostile
  code.** It is meant to catch bugs (infinite loops, accidental file
  writes in the workspace, etc.) in code the *agent itself* generated
  while trying to solve a problem — not to safely execute adversarial
  code from an untrusted third party. Do not repurpose it as one.
- An optional Docker-based sandbox is planned for stronger isolation, but
  Docker is never required for basic installation.

## Safety limits

Configurable via `config.toml` / `.env` (see `.env.example`,
`config.example.toml`), with conservative defaults:

- `allow_web_access`, `allow_code_execution` — hard on/off switches.
- `max_web_requests_per_session`, `max_llm_calls_per_session`,
  `max_iterations` — bound the blast radius and cost of a runaway loop.
- `execution_timeout_seconds` — every sandboxed run is bounded.
- `max_source_size` — refuse to ingest oversized documents.
- `allowed_domains` / `blocked_domains` — optional allow/block lists for
  web research.

## What the agent must never do

- Delete user files outside the configured workspace/vault.
- Modify system settings.
- Install arbitrary software automatically.
- Bypass authentication or paywalls to fetch content.
- Let Critic/Student/Teacher roles assign their own final mastery score
  (see [mastery.md](mastery.md) — this is a correctness guarantee as much
  as a security one: it keeps the system's self-reported state honest).
- Rewrite its own core/evaluator/security modules during a learning
  loop run — those modules are out of scope for any self-modification
  this project performs.

## Reporting a vulnerability

See [SECURITY.md](../SECURITY.md) in the repository root.
