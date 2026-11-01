# Android Application System Design

> *From Fundamentals to Production-Scale Engineering*

This repository holds the manuscript, diagrams, and reference code for a
technically rigorous book on **Android application system design** — aimed at
Senior, Lead, and Staff Android engineers and at engineers preparing for
Senior SDE / SDE-III / Staff / Android-Lead system-design interviews.

## Status

| Phase | Description | State |
|-------|-------------|-------|
| **Phase 1** | Book planning: title, audience, full TOC, 100-topic catalog, dependency ordering, reference application, conventions, glossary | ✅ Draft complete — see [`BLUEPRINT.md`](./BLUEPRINT.md) |
| **Phase 2+** | Chapter-by-chapter authoring (one topic at a time, 18-section structure) | ⏸ Awaiting approval of Phase 1 |

**Nothing beyond the blueprint is written yet.** Per the authoring workflow,
chapters are produced one topic at a time, on request, only after the Phase 1
plan is approved.

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
