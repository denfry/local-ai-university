# Obsidian integration

Obsidian is the primary visual interface to the knowledge graph — not an
optional export format. The design goal is that a standard install of
Obsidian, with no required third-party plugins, shows a meaningful graph
in Graph View just by opening the vault.

## Vault layout

```
<OBSIDIAN_VAULT_PATH>/
├── 00 Dashboard.md
├── Curriculum/
│   ├── Mathematics/
│   ├── Programming/
│   ├── Computer Architecture/
│   ├── Operating Systems/
│   ├── Networks/
│   ├── Databases/
│   ├── Theory of Computation/
│   ├── Software Engineering/
│   └── Advanced Topics/
├── Problems/
├── Mistakes/
├── Learning Log/
└── Sources/
```

## Skill note shape

Each skill is one Markdown note with YAML frontmatter:

```markdown
---
type: skill
domain: algorithms
status: practicing
mastery: 73
confidence: 81
attempts: 34
passed: 26
last_reviewed: 2026-08-08
---

## Summary
...

## Why it matters
...

## Prerequisites
- [[Arrays]]
- [[Loop Invariants]]

## Related topics
- [[Two Pointers]]

## Key concepts
...

## Sources
- [[RFC 791]]

## Current mastery
...

## Evidence
...

## Weak points
...

## Mistakes
- [[Off-by-one Errors]]

## Problems solved
...

## Next steps
...
```

## Why wikilinks, not a plugin-dependent graph

Obsidian's built-in Graph View renders `[[wikilink]]` references between
notes with zero configuration. By making prerequisites, related topics,
mistakes, and sources into real wikilinks, the graph becomes an emergent
property of correctly-written notes rather than something the project has
to draw itself. Example shape:

```
Algorithms
  -> Searching
       -> Binary Search
            -> Arrays
            -> Loop Invariants
```

Mistakes are linked the same way, which is what makes cross-skill root
cause detection visible: if `[[Off-by-one Errors]]` links to `Binary
Search`, `Arrays`, and `Two Pointers`, the graph itself shows the pattern
without any extra tooling.

## Dashboard

`00 Dashboard.md` is regenerated (not hand-edited) and is designed to be
useful with plain Obsidian — no Dataview requirement. It includes:

- overall stats (skills tracked, sessions run, problems attempted),
- current topics and weakest skills,
- recently mastered skills and recent mistakes,
- next objectives,
- the most recent Learning Log entries.

If the user has the Dataview plugin installed, optional Dataview query
snippets may be included as a bonus, but the project must never depend on
it for the vault to be useful.

## Learning Log

After every session, a new `Learning Log/YYYY-MM-DD-HHMMSS.md` file
records what was studied, which sources were used, which problems were
attempted, results, mistakes, the mastery delta, and the reasoning behind
the next topic choice — so the log itself is a readable narrative of the
agent's history, not just a database dump.

## Safety boundary

The vault renderer only ever writes inside `OBSIDIAN_VAULT_PATH`. It does
not touch any other part of the user's Obsidian vault or filesystem.
