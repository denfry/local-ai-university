"""SQLite persistence layer.

Planned tables/entities (see docs/architecture.md), expected to be
modeled with SQLAlchemy or SQLModel:

- skills, prerequisites (curriculum graph)
- learning_sessions
- problems, attempts, evaluations
- mistakes
- sources
- notes
- mastery_history

A schema initialization/migration mechanism is planned but not yet
implemented; no models or repositories exist in this package yet.
"""
