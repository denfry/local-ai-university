# Development guide

## Current state of the repository

This repository currently contains an **architecture scaffold**: package
boundaries, interfaces described in docstrings, prompts, configuration
examples, and documentation. It does not yet contain the learning-loop
implementation. See the root README's "Project status" section before
assuming any CLI command does something.

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -e ".[dev]"
```

## Tooling

- **pytest** / **pytest-cov** for tests (`pytest`, `pytest --cov=aiu`).
- **Ruff** for linting and formatting (`ruff check .`, `ruff format .`).
- **mypy** for type checking (`mypy src`).

All three are expected to pass in CI (`.github/workflows/ci.yml`) without
a running Ollama instance — anything that talks to Ollama must be behind
the `LLMProvider` interface so tests can substitute a fake/mock.

## Implementation order (suggested)

When picking up implementation work, this order keeps each step testable
on its own:

1. `db` — schema + repositories, since almost everything else persists
   through it.
2. `llm` — `LLMProvider` interface, `OllamaProvider`, `FakeProvider`.
3. `curriculum` — Skill graph + seed data from `docs/curriculum.md`.
4. `mastery` — the scoring formula, with tests asserting that low-evidence
   situations produce low confidence (see `docs/mastery.md`).
5. `sandbox` — subprocess sandbox with timeout enforcement, tested first.
6. `agents` — Student/Teacher/Critic/Examiner/Evaluator, each testable
   against a `FakeProvider`.
7. `web` — SearchProvider/ContentFetcher, with source-ranking tests.
8. `obsidian` — vault renderer, tested against a temp directory.
9. `cli` — wire the above into Typer commands (`init`, `doctor`, `status`,
   `curriculum`, `learn`, `exam`, `sync-obsidian`, `sources`, `mistakes`,
   `demo`).

## Minimum test coverage expected before calling a subsystem "done"

- curriculum graph construction and prerequisite lookups,
- mastery formula edge cases (single data point -> low confidence),
- Obsidian renderer output shape (frontmatter fields, wikilinks present),
- SQLite repository round-trips,
- `OllamaProvider` against a mocked HTTP layer (no real Ollama in CI),
- source ranking given a fixed set of candidate sources,
- safety limits (e.g. a session actually stops at `max_iterations`),
- sandbox timeout enforcement,
- exam-mode isolation (no episodic memory / lesson access leaks in).

## Git workflow

Small, meaningful commits over one giant commit. Conventional-ish
prefixes are used in this repo's history (`feat:`, `fix:`, `docs:`,
`test:`, `ci:`, `chore:`) — match that style for new commits.
