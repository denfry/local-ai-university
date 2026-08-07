"""Configuration loading for Local AI University.

Intended responsibilities (not yet implemented):

- Load settings from `config.toml` (see config.example.toml) and environment
  variables (see .env.example), with environment variables taking
  precedence over file values.
- Expose typed configuration sections: `[ollama]`, `[learning]`, `[web]`,
  `[obsidian]`, `[sandbox]`.
- Enforce safety defaults described in docs/security.md, such as
  `max_web_requests_per_session`, `max_llm_calls_per_session`,
  `execution_timeout_seconds`, `allowed_domains`, and `blocked_domains`.
- Never read secrets from source control; `.env` is gitignored.
"""
