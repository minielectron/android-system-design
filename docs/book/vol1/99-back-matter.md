# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is treated. (Chapter numbers outside this volume's range point to other volumes of the series.)

**Backoff** — Progressively increasing the delay between retries (often exponential, with jitter) to avoid hammering a failing server. Ch 2.

**Circuit breaker** — A reliability pattern that stops calling a failing dependency for a cooldown, then probes before resuming. Ch 2.

**Coroutine** — Kotlin's unit of structured, cancellable asynchronous work; the foundation of off-main-thread execution. Ch 3.

**Debounce** — Waiting for input to settle before acting, so rapid events (keystrokes) collapse into one action. Ch 9.

**Dependency injection (DI)** — Supplying an object's dependencies from outside rather than constructing them internally; here via Hilt. Ch 5.

**DataStore** — The modern typed replacement for SharedPreferences, for app configuration (Preferences and Proto). Ch 4.

**Flow** — A cold, asynchronous stream of values in Kotlin coroutines; the backbone of reactive data. Ch 3, Ch 6.

**Idempotency key** — A client-supplied key that lets a server safely de-duplicate retried mutations. Ch 15; applied to checkout in Ch 75.

**Interceptor** — An OkHttp hook that observes or modifies requests/responses; application vs network interceptors. Ch 1.

**Mapper / DTO** — A DTO is the wire shape of data; a mapper converts DTOs to domain models, isolating the app from API changes. Ch 1, Ch 16.

**Pagination** — Loading a large list in pages as the user scrolls, bounding memory and network. Ch 13.

**Process death** — The OS reclaiming a backgrounded app's process; state must be restored on return. Ch 8.

**Repository** — The data layer's single entry point for a domain type; owns the sources, exposes the single source of truth. Ch 1, Ch 3.

**Result / Outcome type** — A uniform success/failure return type that keeps exceptions out of domain and UI. Ch 1.

**Retrofit** — A declarative HTTP client that turns a Kotlin interface into networked calls over OkHttp. Ch 1.

**Request de-duplication** — Collapsing concurrent identical in-flight requests into one shared call. Ch 11.

**Single source of truth (SSOT)** — One authoritative local store (Room) that the UI reads from; the network updates it, the UI observes it. Ch 3.

**StateFlow / UDF** — A hot, state-holding Flow driving unidirectional data flow — state down, events up. Ch 6.

**Timeout (call/connect/read/write)** — Bounds on how long a network operation may take; callTimeout bounds the whole call. Ch 1, Ch 2.

**Resumable upload** — An upload that can continue from where it left off after interruption. Ch 17; downloads in Ch 18.


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

- **Volume 2 — Security, Offline-First & State** (Chapters 19–43) — authentication and token management, cryptography and the Keystore, secure storage and PII handling, offline-first architecture, the outbox pattern, delta sync and conflict resolution, and shared/global state.

- **Volume 3 — Lifecycle, Background & Media** (Chapters 44–62) — the Android lifecycle and startup, foreground and background work, WorkManager, Doze and background limits, notifications, deep links and navigation, plus media playback with Media3/ExoPlayer, DRM, the camera, and file handling.

- **Volume 4 — Real-Time & Feature Architectures** (Chapters 63–81) — WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, reviews, and onboarding.

- **Volume 5 — Performance, Scale & Platform Breadth** (Chapters 82–100) — analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, battery, baseline profiles, modularization, localization, accessibility, theming, Android TV and Wear OS, and the end-to-end StreamCart capstone.

All five volumes build on the **StreamCart** reference application and the foundations introduced in Volume 1.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a rating or review.*

