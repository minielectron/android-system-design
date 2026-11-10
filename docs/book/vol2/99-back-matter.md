# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is treated. (Chapter numbers outside this volume's range point to other volumes of the series.)

**Access / refresh token** — Short-lived access tokens with a longer-lived refresh token; refreshed transparently on 401. Ch 19.

**Android Keystore** — Hardware-backed secure storage for cryptographic keys; keys never leave secure hardware. Ch 20.

**Biometric authentication** — Fingerprint/face authentication gating sensitive actions, tied to a Keystore key. Ch 21.

**Session management** — Tracking active sessions and supporting logout-everywhere across devices. Ch 22.

**Certificate pinning** — Restricting trust to specific server certificates/keys to resist MITM. Ch 23.

**Encryption at rest** — Encrypting the local database/files (e.g. SQLCipher) so data is useless if the device is compromised. Ch 24, Ch 25.

**App integrity / root detection** — Verifying the app and device are untampered (Play Integrity, root checks). Ch 26.

**R8 / obfuscation** — Shrinking and obfuscating release code; raises the reverse-engineering bar (not a secret store). Ch 27.

**PII redaction** — Scrubbing personally identifiable information from logs and telemetry. Ch 28.

**Offline-first** — Treating the local store as the source of truth so the app works without a network. Ch 29.

**WorkManager** — The deferrable, guaranteed background-work scheduler used for sync. Ch 30.

**Outbox pattern** — Writing a mutation locally plus a pending operation, then syncing it reliably (with retries). Ch 31.

**Delta / incremental sync** — Transferring only what changed since the last sync, not the full dataset. Ch 32.

**Conflict resolution** — Reconciling concurrent edits (last-writer-wins, merges, versioning) in a sync engine. Ch 33.

**Cache invalidation** — Deciding when cached data is stale and must be refetched or evicted. Ch 34.

**Full-text search (FTS)** — Indexed local text search over Room data. Ch 35.

**Room migration** — Evolving the local database schema safely across app versions. Ch 36.

**Backup / export** — Exporting, importing, and backing up user data. Ch 37.

**Feature flags / remote config** — Toggling features and tuning behavior remotely without an app update. Ch 41.

**Multi-account isolation** — Keeping each account's data strictly separate; clearing on switch/sign-out. Ch 42.

**Shared ViewModel scope** — Sharing state across screens via a ViewModel scoped to a navigation graph or activity. Ch 38, Ch 40.


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

- **Volume 3 — Lifecycle, Background & Media** (Chapters 44–62) — the Android lifecycle and startup, foreground and background work, WorkManager, Doze and background limits, notifications, deep links and navigation, plus media playback with Media3/ExoPlayer, DRM, the camera, and file handling.

- **Volume 4 — Real-Time & Feature Architectures** (Chapters 63–81) — WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, reviews, and onboarding.

- **Volume 5 — Performance, Scale & Platform Breadth** (Chapters 82–100) — analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, battery, baseline profiles, modularization, localization, accessibility, theming, Android TV and Wear OS, and the end-to-end StreamCart capstone.

All five volumes build on the **StreamCart** reference application and the foundations introduced in Volume 1.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a rating or review.*

