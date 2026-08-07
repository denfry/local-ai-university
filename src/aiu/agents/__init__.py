"""Agent roles that make up the learning loop.

Planned modules, one per role (see docs/architecture.md for the full
learning-loop sequence):

- `orchestrator.py` — drives the end-to-end learning loop: pick a topic,
  gather sources, run study/practice/exam phases, persist results,
  sync Obsidian, choose the next objective. Owns iteration/budget limits.
- `student.py`      — attempts problems, with or without access to the
  freshly studied lesson and past memory, depending on mode
  (practice vs. exam).
- `teacher.py`       — turns vetted sources into a structured lesson for
  a topic. Disabled entirely during exams.
- `critic.py`        — analyzes Student's incorrect attempts and proposes
  root causes / remediation. Cannot assign mastery itself.
- `examiner.py`      — generates exam problems that are distinct from the
  practice examples the Student has already seen.
- `evaluator.py`     — objectively grades attempts using external tools
  (pytest/hidden tests for code, SymPy/numeric checks for math), never
  by asking the LLM whether an answer is correct.

None of these roles are implemented yet; this package only fixes the
module boundaries and responsibilities.
"""
