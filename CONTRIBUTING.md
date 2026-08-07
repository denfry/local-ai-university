# Contributing

Thanks for considering a contribution to Local AI University.

## Current state

This project is at the architecture-scaffold stage (see the README's
"Project status"). That means most contributions right now are either:

1. Implementing one of the modules described in
   [docs/development.md](docs/development.md)'s suggested order, or
2. Improving the design docs / prompts themselves before code is written
   against them.

If you're picking up an implementation task, check open issues first so
two people don't build the same module in parallel.

## Setup

```bash
pip install -e ".[dev]"
pytest
ruff check .
mypy src
```

All three must pass before opening a PR. CI runs the same checks and must
not require a running Ollama instance — anything touching Ollama should
go through `LLMProvider` so tests can use a fake/mock implementation.

## Guidelines

- Keep modules aligned with the responsibilities documented in their
  `__init__.py` and in `docs/architecture.md`. If you need to deviate,
  update the docs in the same PR.
- Never have the LLM assign its own mastery/correctness verdict — see
  [docs/mastery.md](docs/mastery.md).
- Treat all fetched web content as untrusted data — see
  [docs/security.md](docs/security.md).
- Any code execution must go through `CodeSandbox` with a timeout; never
  add a raw `exec()`/`eval()` path over LLM output.
- Add tests alongside new behavior — see the "minimum test coverage"
  list in [docs/development.md](docs/development.md).
- Keep commits focused; prefer several small, well-described commits
  over one large one.

## Reporting bugs / requesting features

Use the issue templates. For security issues, see
[SECURITY.md](SECURITY.md) instead of opening a public issue.

## Code of conduct

Participation in this project is governed by
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
