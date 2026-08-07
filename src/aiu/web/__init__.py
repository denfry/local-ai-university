"""Web research abstraction: search and content fetching.

Planned interfaces (see docs/web-research.md):

- `SearchProvider` — abstract interface for querying the web, so the
  backend (search engine/API) is swappable and not hard-wired into core
  logic. At least one non-paid-LLM-API-dependent implementation is
  planned.
- `ContentFetcher` — retrieves and extracts readable content from a URL,
  respecting timeouts, maximum document size, and HTTP errors, without
  bypassing authentication or paywalls.
- Source metadata capture: URL, title, author, publication/update date,
  retrieved_at, source type, trust score, relevance score — with source
  priority favoring official docs/RFCs/standards over general web pages.

All fetched content is treated as untrusted DATA, never as instructions
to the agent — see docs/security.md ("Prompt Injection and Untrusted
Sources"). No search or fetch logic is implemented yet.
"""
