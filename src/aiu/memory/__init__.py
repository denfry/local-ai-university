"""Mistake and long-term memory tracking.

Planned responsibilities:

- `Mistake` entity: category, description, root_cause, skill,
  occurrences, first_seen, last_seen, remediation, resolved_status.
- Cross-skill mistake correlation: detect when the same root cause
  (e.g. off-by-one, wrong loop invariant, recursion base case) recurs
  across otherwise unrelated skills, so the Obsidian graph can link them.
- Separation of episodic memory (past specific sessions/attempts) from
  semantic memory (consolidated lesson/skill knowledge) and procedural
  memory (how to approach a class of problems) — episodic memory is
  disabled during exams.

No storage or detection logic is implemented yet.
"""
