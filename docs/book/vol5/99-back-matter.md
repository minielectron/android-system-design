# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is treated. (Chapter numbers outside this volume's range point to other volumes of the series.)

**Analytics pipeline** — A reliable, batched, consented, PII-safe path for events. Ch 82.

**Crash / ANR reporting** — Capturing fatal crashes and Application-Not-Responding errors from the field. Ch 83.

**Distributed tracing** — Correlating a request across client and services via trace/correlation IDs. Ch 84.

**Percentiles (p95/p99)** — Tail latency metrics; the tail, not the average, is where users suffer. Ch 85.

**Real-user monitoring (RUM)** — Measuring performance from real users in the field, not just the lab. Ch 85.

**A/B testing** — Comparing variants with sticky assignment, guardrails, and significance. Ch 86.

**Error fingerprinting** — Grouping identical errors by a stable signature so thousands collapse to one issue. Ch 87.

**TTID / TTFD** — Time to initial display and time to full display — key startup metrics. Ch 88.

**Memory leak / LeakCanary** — A reachable object that should be freed; detected with LeakCanary. Ch 89.

**Recomposition / jank** — Excess Compose recomposition and dropped frames that cause stutter. Ch 90.

**Radio tail** — The cellular radio staying in a high-power state for seconds after a transfer. Ch 91.

**Baseline Profile** — A list of startup/critical-path methods AOT-compiled at install for a fast first launch. Ch 92.

**Lazy list** — A recycling list (LazyColumn) that composes only visible items with stable keys. Ch 93.

**Multi-module architecture** — Splitting the app into app/feature/core Gradle modules with a one-way dependency graph. Ch 94.

**Localization / RTL** — Translating and mirroring the UI for every language and direction. Ch 95.

**Accessibility / semantics** — The semantics tree that screen readers consume; targets, contrast, scalable text. Ch 96.

**Design tokens / theming** — A single source of color/type/shape tokens driving the whole UI, with dark/dynamic color. Ch 97.

**D-pad focus** — The focus-state model that drives TV/STB navigation with a remote. Ch 98.

**Wear Data Layer** — The API that syncs small state between a phone and a Wear OS watch. Ch 99.

**Capstone** — The end-to-end StreamCart system design that composes the whole book. Ch 100.


---

# Acknowledgements

This book exists because of the Android engineering community — the library authors, the writers
of official documentation and release notes, the conference speakers, and the countless engineers
who have shared hard-won lessons in blog posts, talks, and code reviews. The patterns in this
series are not invented in isolation; they are the distilled, composed practice of that community,
organized into one coherent curriculum.

Special thanks to the maintainers of the open-source libraries this book builds on — including
Kotlin and Coroutines, Jetpack (Compose, Room, WorkManager, Paging, Lifecycle), OkHttp and
Retrofit, Hilt/Dagger, and Media3 — whose work makes modern Android development what it is.

And thank you, the reader, for investing in the craft of building software that lasts.


---

# About the Author

Prakash Sharma is a Senior Software Engineer at Deutsche Telekom with a decade of experience building Android applications across mobile, television (TV), and set-top-box (STB) platforms. Over those years he has shipped and maintained large, long-lived Android codebases — the kind where architecture, offline behavior, security, performance, and multi-team maintainability are not optional extras but the whole job.

He writes about Android architecture and engineering on **Medium**, and is the author of technical books on modern Android development. He wrote *Designing Android at Scale* to close the gap he kept seeing — and interviewing for — between *knowing Android APIs* and *designing systems* that survive real-world scale, constraints, and teams.

*Follow Prakash on **Medium** for articles, updates, and corrections to this series: {{MEDIUM PROFILE URL}}*


---

# Also in This Series

If this volume was useful, the series continues:

- **Volume 1 — Foundations: Networking & Local Data** (Chapters 1–18) — the networking core, persistence and the single source of truth, threading, dependency injection, and the networking patterns layered on top — search, pagination, caching, and reliability.

- **Volume 2 — Security, Offline-First & State** (Chapters 19–43) — authentication and token management, cryptography and the Keystore, secure storage and PII handling, offline-first architecture, the outbox pattern, delta sync and conflict resolution, and shared/global state.

- **Volume 3 — Lifecycle, Background & Media** (Chapters 44–62) — the Android lifecycle and startup, foreground and background work, WorkManager, Doze and background limits, notifications, deep links and navigation, plus media playback with Media3/ExoPlayer, DRM, the camera, and file handling.

- **Volume 4 — Real-Time & Feature Architectures** (Chapters 63–81) — WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, reviews, and onboarding.

All five volumes build on the **StreamCart** reference application and the foundations introduced in Volume 1.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a rating or review.*

