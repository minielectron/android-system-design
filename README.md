# Designing Android at Scale

> *System Design in Practice: Building, and Defending Production-Scale Mobile Features in Kotlin*

This repository holds the manuscript, diagrams, and reference code for a
technically rigorous book on **Android application system design** — aimed at
Senior, Lead, and Staff Android engineers and at engineers preparing for
Senior SDE / SDE-III / Staff / Android-Lead system-design interviews.

## Status

| Phase | Description | State |
|-------|-------------|-------|
| **Phase 1** | Book planning: title, audience, full TOC, 100-topic catalog, dependency ordering, reference application, conventions, glossary | ✅ Approved — see [`BLUEPRINT.md`](./BLUEPRINT.md) |
| **Phase 2+** | Chapter-by-chapter authoring (one topic at a time, 18-section structure) | 🚧 In progress |

### Chapters authored

| Ch | Topic | File | State |
|----|-------|------|-------|
| 1 | Networking Core: API Request Orchestration | [`docs/chapters/01-networking-core.md`](./docs/chapters/01-networking-core.md) | ✅ Draft |
| 2 | Network Reliability: Timeouts, Retries, Backoff & Circuit Breaking | [`docs/chapters/02-network-reliability.md`](./docs/chapters/02-network-reliability.md) | ✅ Draft |
| 3 | Persistence Core & Single Source of Truth | [`docs/chapters/03-persistence-core-ssot.md`](./docs/chapters/03-persistence-core-ssot.md) | ✅ Draft |
| 4 | DataStore: Preferences & Proto | [`docs/chapters/04-datastore.md`](./docs/chapters/04-datastore.md) | ✅ Draft |
| 5 | Dependency Injection at Scale with Hilt | [`docs/chapters/05-dependency-injection-hilt.md`](./docs/chapters/05-dependency-injection-hilt.md) | ✅ Draft |
| 6 | UI State Modeling & Unidirectional Data Flow | [`docs/chapters/06-ui-state-udf.md`](./docs/chapters/06-ui-state-udf.md) | ✅ Draft |
| 7 | One-Time Events & Side Effects | [`docs/chapters/07-one-time-events.md`](./docs/chapters/07-one-time-events.md) | ✅ Draft |
| 8 | Process Death & State Restoration | [`docs/chapters/08-process-death-state-restoration.md`](./docs/chapters/08-process-death-state-restoration.md) | ✅ Draft |
| 9 | Debounced Network Search | [`docs/chapters/09-debounced-network-search.md`](./docs/chapters/09-debounced-network-search.md) | ✅ Draft |
| 10 | Search Suggestions & Autocomplete | [`docs/chapters/10-search-suggestions-autocomplete.md`](./docs/chapters/10-search-suggestions-autocomplete.md) | ✅ Draft |
| 11 | Request Deduplication & Single-Flight | [`docs/chapters/11-request-deduplication-single-flight.md`](./docs/chapters/11-request-deduplication-single-flight.md) | ✅ Draft |
| 12 | Caching Strategies: HTTP, In-Memory, Disk | [`docs/chapters/12-caching-strategies.md`](./docs/chapters/12-caching-strategies.md) | ✅ Draft |
| 13 | Pagination & Caching with Paging 3 | [`docs/chapters/13-pagination-paging3.md`](./docs/chapters/13-pagination-paging3.md) | ✅ Draft |
| 14 | Request Prioritization, Queueing & Rate Limiting | [`docs/chapters/14-request-prioritization-rate-limiting.md`](./docs/chapters/14-request-prioritization-rate-limiting.md) | ✅ Draft |

> Chapters are authored one topic at a time (or in batches on request). The
> chapter numbering follows the blueprint's canonical order (§5); authoring order
> can differ — Ch 9 (Debounced Search) was authored first, then the Part I
> foundations (Ch 1–5) it depends on.

### Formats

- **Markdown** (`docs/chapters/*.md`) — diagrams are embedded inline as base64
  PNGs, so each chapter renders self-contained in any markdown viewer.
- **PDF** (`docs/pdf/*.pdf`) — a book-styled, self-contained PDF per chapter
  (plus the blueprint), generated from the markdown with diagrams baked in.

> Diagrams are authored in Mermaid, rendered to PNG, and embedded; the render/
> embed/PDF pipeline is reusable for every new chapter.

## How this book is organized

- Every **topic is one chapter**, and every chapter follows the same
  **18-section mandatory structure** (problem → requirements → architecture →
  Kotlin implementation → concurrency → failure recovery → scaling →
  trade-offs → security → performance → testing → observability → interview
  prep → exercises → summary).
- All chapters share **one reference application — *StreamCart*** — a fictional
  super-app that combines e-commerce and content streaming, so patterns can be
  demonstrated across realistic modules instead of toy examples.
- Shared infrastructure (networking core, persistence core, DI, error model,
  logging) is defined once in **Part I** and **reused and extended** by later
  chapters rather than reinvented.

## Repository layout (planned)

```
.
├── README.md                 # this file
├── BLUEPRINT.md              # Phase 1 deliverable: the complete book plan
├── docs/
│   ├── conventions/          # code + diagram conventions (expanded from blueprint)
│   └── chapters/             # one markdown file per chapter, added as authored
│       └── NN-topic-slug.md
└── reference-app/            # StreamCart reference code modules (added incrementally)
```

> The `docs/chapters/` and `reference-app/` trees are created as chapters are
> written. They are intentionally empty today.

## Conventions at a glance

- **Language:** Kotlin, structured concurrency, Flow/StateFlow/SharedFlow.
- **UI:** Jetpack Compose, unidirectional data flow.
- **Architecture:** Multi-module Clean Architecture (applied pragmatically, not
  dogmatically).
- **DI:** Hilt. **Persistence:** Room + DataStore. **Background:** WorkManager.
  **Networking:** OkHttp + Retrofit + Kotlin Serialization.
- **Diagrams:** Mermaid throughout (architecture, class, sequence, state,
  data-flow, failure-recovery).

See [`BLUEPRINT.md`](./BLUEPRINT.md) §7–§9 for the full reference architecture,
code conventions, and diagram conventions.
