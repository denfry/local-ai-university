# Web research

The agent does not browse the web directly with the LLM; it uses two
small abstractions so the underlying backends can be swapped without
touching core logic.

## `SearchProvider`

An interface for turning a query into a ranked list of candidate URLs.
The core project does not hard-wire itself to one search engine or
require a paid LLM-bundled search API; at least one implementation that
doesn't require a paid API key is planned for the MVP.

## `ContentFetcher`

An interface for retrieving and extracting readable content from a URL.
Expected constraints:

- respects a request timeout,
- enforces a maximum document size (`max_source_size`),
- surfaces HTTP errors instead of silently swallowing them,
- never attempts to bypass authentication or paywalls,
- does not attempt to download or mirror entire sites — one page/document
  at a time, on demand.

## Source metadata

For every candidate source, the pipeline is expected to record:

- URL, title, author (if available), publication/update date (if
  available),
- `retrieved_at` (when *this* agent fetched it),
- source type (official docs, standard/RFC, university material,
  textbook, paper, other technical resource, general web),
- trust score and relevance score, produced by the source evaluator
  (`prompts/source_evaluator.md`).

## Source priority

Roughly, in order of default trust:

1. Official documentation.
2. Standards and RFCs.
3. University course materials.
4. Open textbooks.
5. Papers.
6. Other reputable technical resources.
7. Everything else.

The agent should not blindly trust the first result it finds, and for
load-bearing factual claims should prefer corroboration from more than
one independent source over relying on a single strong one.

## Untrusted by default

All fetched content is treated as data, never as instructions — see
[security.md](security.md#prompt-injection-and-untrusted-sources) for the
full prompt-injection stance. This applies uniformly regardless of how
trustworthy the source scored: trust score affects whether a fact gets
used in a lesson, not whether the raw text is allowed to influence the
agent's behavior directly.
