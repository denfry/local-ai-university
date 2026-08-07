"""Command-line interface for Local AI University.

Planned Typer-based entry point (`aiu`) exposing the following commands,
each to be implemented as a separate module in this package:

- `aiu init`            — scaffold config files and workspace directories.
- `aiu doctor`           — verify Ollama, the model, Obsidian vault, DB,
                            Python, and sandbox availability.
- `aiu status`           — show model, progress, current/weakest topics,
                            and recent sessions.
- `aiu curriculum`       — display the curriculum knowledge graph.
- `aiu learn`            — run a learning session (`--topic`, `--iterations`).
- `aiu exam <topic>`     — run an isolated exam session (no hints, no
                            episodic memory, no web access).
- `aiu sync-obsidian`    — regenerate the Obsidian vault from the database.
- `aiu sources <topic>`  — list sources used for a topic.
- `aiu mistakes`         — show recurring mistakes across skills.
- `aiu demo`             — run an offline demo using a fake LLM provider.

No command logic is implemented yet; this module only records the intended
CLI surface for the MVP described in docs/architecture.md.
"""
