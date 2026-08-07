"""Obsidian vault renderer — the visual interface to the knowledge graph.

Planned responsibilities (see docs/obsidian.md):

- Render `Skill`, `Mistake`, `Problem`, and `Source` records as Markdown
  notes with YAML frontmatter (type, domain, status, mastery, confidence,
  attempts, passed, last_reviewed) under a fixed vault layout: Curriculum
  domain folders, Problems/, Mistakes/, Learning Log/, Sources/.
- Use Obsidian wikilinks (`[[Skill Name]]`) between skills, prerequisites,
  related topics, mistakes, and sources so the built-in Graph View shows
  a meaningful, navigable graph without requiring third-party plugins.
- Regenerate `00 Dashboard.md` (stats, current topics, weakest skills,
  recently mastered, recent mistakes, next objectives) and append a
  timestamped `Learning Log/YYYY-MM-DD-HHMMSS.md` entry per session.
- Never touches files outside the configured `OBSIDIAN_VAULT_PATH`.

No rendering logic is implemented yet.
"""
