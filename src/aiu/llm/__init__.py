"""LLM provider abstraction layer.

Design (see docs/architecture.md):

- `LLMProvider` — an abstract interface (e.g. `complete`, `chat`,
  `embed` if/when needed) that all providers implement, so the rest of
  the system never depends on a specific backend.
- `OllamaProvider` — the default implementation, talking to a local
  Ollama server over HTTP (httpx). Configured via `OLLAMA_BASE_URL`,
  `OLLAMA_MODEL`, `OLLAMA_TEMPERATURE`, `OLLAMA_CONTEXT_LENGTH`.
- A `FakeProvider` (used by `aiu demo` and tests) that returns canned
  responses without any network access or running Ollama instance.

No provider is implemented yet — this package currently only reserves the
module layout: `base.py`, `ollama_provider.py`, `fake_provider.py`.
"""
