"""Curriculum knowledge graph for Computer Science & Computer Engineering.

Intended responsibilities (see docs/curriculum.md):

- Define the `Skill` entity (id, title, slug, domain, description,
  prerequisites, related_skills, mastery, confidence, status, attempts,
  successful_attempts, last_reviewed_at, created_at, updated_at) and its
  status lifecycle: discovered -> studying -> practicing -> proficient
  -> mastered.
- Model the curriculum as a directed graph (prerequisites/related edges),
  not a flat list, seeded from the top-level domains: Mathematical
  Foundations, Programming, Computer Architecture, Operating Systems,
  Networks, Databases, Theory of Computation, Software Engineering, and
  Advanced Topics.
- Provide topic-selection logic: find weak prerequisites and pick the
  next topic to study given current mastery/confidence across the graph.

No graph storage or selection logic is implemented yet.
"""
