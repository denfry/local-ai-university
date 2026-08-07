# Curriculum

The curriculum is a directed graph of `Skill` nodes, not a flat list. Each
skill records its own prerequisites and related skills so that both the
topic-selection logic and the Obsidian Graph View reflect real conceptual
dependencies rather than an arbitrary ordering.

## Skill fields

| Field                 | Purpose                                              |
|-----------------------|-------------------------------------------------------|
| `id`, `slug`          | Stable identifiers, `slug` used for filenames/links   |
| `title`               | Display name                                          |
| `domain`              | Top-level curriculum domain (see below)               |
| `description`         | Short summary of what the skill covers                |
| `prerequisites`       | Skill ids that should be reasonably solid first        |
| `related_skills`      | Non-prerequisite conceptual neighbors                  |
| `mastery`             | 0-100, computed — see [mastery.md](mastery.md)         |
| `confidence`          | 0-100, how much evidence backs the mastery number      |
| `status`              | discovered / studying / practicing / proficient / mastered |
| `attempts`, `successful_attempts` | Raw counters feeding mastery         |
| `last_reviewed_at`    | Drives recency weighting and spaced review candidates  |
| `created_at`, `updated_at` | Bookkeeping                                       |

## Status lifecycle

```
discovered -> studying -> practicing -> proficient -> mastered
```

A skill can be re-added to `studying` or `practicing` if new mistakes or
a failed exam reveal it isn't as solid as its status implied — the graph
is expected to move backward as well as forward.

## Starting domains

1. **Математическая база** — дискретная математика, математическая
   логика, линейная алгебра, математический анализ, теория вероятностей,
   комбинаторика.
2. **Программирование** — Python, C, C++, структуры данных, алгоритмы,
   рекурсия, complexity analysis, OOP, functional programming basics.
3. **Архитектура вычислительных систем** — Boolean algebra, digital
   logic, number representation, CPU, ISA, assembly, memory hierarchy,
   cache, virtual memory basics.
4. **Операционные системы** — processes, threads, scheduling,
   synchronization, deadlocks, virtual memory, filesystems.
5. **Компьютерные сети** — OSI/TCP-IP concepts, Ethernet, IP, TCP, UDP,
   DNS, HTTP, routing, sockets.
6. **Базы данных** — relational model, SQL, indexes, transactions,
   normalization, query planning.
7. **Теория вычислений** — automata, formal languages, computability,
   complexity theory.
8. **Software Engineering** — Git, testing, debugging, architecture,
   design principles, CI/CD.
9. **Продвинутые темы** — distributed systems, compilers, cybersecurity
   fundamentals, machine learning fundamentals, parallel computing, GPU
   computing.

This is a starting seed, not a ceiling: the curriculum module is expected
to grow the graph over time when a lesson surfaces a concept that isn't
tracked yet (see `prompts/curriculum.md` for how that suggestion flow is
meant to work).

## Topic selection (target behavior)

Given the graph and current mastery/confidence values, the next-topic
choice should prefer, roughly in order:

1. Skills whose prerequisites are weak (low mastery/confidence) — study
   the prerequisite before the dependent skill.
2. Skills that have stalled (multiple failed attempts without recent
   improvement) over brand-new topics, so recurring mistakes get
   addressed before the graph grows wider.
3. Breadth within the current domain before jumping to an unrelated
   domain, unless the user explicitly requests a topic via
   `aiu learn --topic "..."`.

This logic is not implemented yet; `src/aiu/curriculum/__init__.py`
reserves the module for it.
