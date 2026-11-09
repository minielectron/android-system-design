# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is
treated. (Chapter numbers above 18 point to later volumes of the series.)

**Backoff** — Progressively increasing the delay between retries (often exponential, with jitter)
to avoid hammering a failing server. Ch 2.

**Backpressure** — Handling a producer that emits faster than a consumer can process, without
unbounded buffering. Ch 3, Ch 13.

**Cache invalidation** — Deciding when cached data is stale and must be refetched or evicted; the
*strategy* (what/when), distinct from the HTTP cache mechanism. Ch 12.

**Circuit breaker** — A reliability pattern that stops calling a failing dependency for a cooldown
period after repeated failures, then probes before fully resuming. Ch 2.

**Coroutine** — Kotlin's unit of structured, cancellable asynchronous work; the foundation of
off-main-thread execution. Ch 3.

**Debounce** — Waiting for input to settle (a quiet interval) before acting, so rapid events
(keystrokes) collapse into one action. Ch 9.

**Dependency injection (DI)** — Supplying an object's dependencies from outside rather than
constructing them internally; here via Hilt. Ch 5.

**Dispatcher** — The thread pool a coroutine runs on (e.g. `Dispatchers.IO` for blocking I/O,
`Default` for CPU work). Ch 3.

**Flow** — A cold, asynchronous stream of values in Kotlin coroutines; the backbone of reactive
data in this architecture. Ch 3, Ch 6.

**Idempotency key** — A client-supplied key that lets a server safely de-duplicate retried
mutations, giving exactly-once semantics. Ch 15; applied to checkout in Ch 75.

**Interceptor** — An OkHttp hook that observes or modifies requests/responses; *application*
interceptors run once per logical call, *network* interceptors once per hop. Ch 1.

**Mapper / DTO** — A data-transfer object is the wire shape of data; a mapper converts DTOs to
domain models, isolating the app from API changes. Ch 1, Ch 6.

**Optimistic concurrency** — Assuming writes won't conflict, proceeding, and reconciling if a
version mismatch is detected. Ch 15; conflict resolution in Ch 33.

**Pagination** — Loading a large list in pages as the user scrolls, bounding memory and network.
Ch 13; Paging 3 and large lists in Ch 71, Ch 93.

**Repository** — The data layer's single entry point for a domain type; it owns the sources and
exposes the single source of truth. Ch 1, Ch 3.

**Result / Outcome type** — A uniform success/failure return type that keeps exceptions out of the
domain and UI and makes error handling exhaustive. Ch 1, Ch 23.

**Retrofit** — A declarative HTTP client that turns a Kotlin interface into networked calls over
OkHttp. Ch 1.

**Retry** — Re-attempting a failed, *retryable* request (e.g. a timeout or 5xx), ideally with
backoff and a bound. Ch 2.

**Single source of truth (SSOT)** — The principle that one authoritative local store (here, Room)
is the one place the UI reads from; the network updates it, the UI observes it. Ch 3, Ch 5;
offline-first in Ch 29.

**StateFlow** — A hot, state-holding Flow that always has a current value; the standard way a
ViewModel exposes UI state. Ch 6.

**Structured concurrency** — Scoping coroutines to a lifecycle so they are cancelled together and
none are leaked. Ch 3.

**Thundering herd** — Many clients retrying or refreshing at once and overwhelming a server;
mitigated with jitter and request de-duplication. Ch 2, Ch 14.

**Timeout (call / connect / read / write)** — Bounds on how long a network operation may take;
`callTimeout` bounds the entire call, the others bound individual phases. Ch 1, Ch 2.

**Request de-duplication** — Collapsing concurrent identical in-flight requests into one shared
call. Ch 11.

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

{{AUTHOR BIO — replace this with your bio. Suggested content: your name, years of Android
experience, the kinds of apps and platforms you've shipped (mobile, TV, STB, Fire TV, Wear), your
areas of depth (Kotlin, Java, architecture), and a line on why you wrote this series. Example
opening: "{{AUTHOR NAME}} is an Android engineer with over eight years of experience building
production applications across phones, TV, set-top boxes, and wearables..."}}

*Connect / errata:* {{OPTIONAL — website, GitHub, LinkedIn, or contact for corrections and
updates.}}

---

# Also in This Series

If this volume was useful, the series continues:

- **Volume 2 — Security, Offline-First & State** (Chapters 19–43): authentication, cryptography
  and the Keystore, secure storage and PII, offline-first architecture, the outbox pattern, delta
  sync and conflict resolution, and shared/global state.
- **Volume 3 — Lifecycle, Background & Media** (Chapters 44–62): lifecycle and process death,
  WorkManager, Doze, notifications, navigation, and media playback with Media3/ExoPlayer and DRM.
- **Volume 4 — Real-Time & Feature Architectures** (Chapters 63–81): WebSocket/SSE, presence, live
  location, BLE, and the commerce feature stack — feeds, recommendations, cart, checkout,
  payments, and order tracking.
- **Volume 5 — Performance, Scale & Platform Breadth** (Chapters 82–100): analytics, crash,
  tracing, performance, memory, rendering, battery, baseline profiles, modularization,
  localization, accessibility, theming, Android TV and Wear OS, and the end-to-end capstone.

All five volumes build on the **StreamCart** reference application introduced in this volume.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a
rating or review.*
